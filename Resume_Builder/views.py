from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.template.loader import render_to_string
from weasyprint import HTML
from django.core.files.base import ContentFile
from .models import CustomResume, CustomUser
from .serializers import CustomResumeSerializer




class CustomResumeCreateOrUpdateView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        user_id = request.data.get("user")
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "Invalid user_id"}, status=400)

        # Delete previous resume if it exists
        CustomResume.objects.filter(user=user).delete()

        # Create new resume
        resume = CustomResume.objects.create(
            user=user,
            full_name=request.data.get("full_name", ""),
            email=request.data.get("email", ""),
            phone=request.data.get("phone", ""),
            address=request.data.get("address", ""),
            photo=request.FILES.get("photo"),
            skilss=request.data.get("skilss", ""),
        )

        # Generate PDF
        html = render_to_string("custom_resume_template.html", {"resume": resume})
        pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf()
        resume.generated_pdf.save("resume.pdf", ContentFile(pdf))
        resume.save()

        return Response(CustomResumeSerializer(resume).data, status=201)
    
    
class CustomResumeDetailView(APIView):
    def get(self, request):
        user_id = request.GET.get("user")  
        if not user_id:
            return Response({"error": "User ID is required"}, status=400)

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"error": "Invalid user ID"}, status=400)

        try:
            resume = CustomResume.objects.get(user=user)
        except CustomResume.DoesNotExist:
            return Response({"error": "Resume not found for this user"}, status=404)

        return Response(CustomResumeSerializer(resume).data)