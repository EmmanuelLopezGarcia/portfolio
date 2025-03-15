from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.

def index(request):

    return render (request, "index.html")


def about(request):

    return render (request, "about.html")

def projects(request):

    all_projects = [

        {"title":"TravelShopProject", "image":"images/travel_project.jpeg"},
        {"title":"Portfolio", "image":"images/portfolio.PNG"},
        {"title":"YoutubeChannel", "image": "images/youtube_channel.png"},

    ]

    return render (request, "projects.html", {"projects": all_projects})

def experiences(request):

    experiences = [

        {"company": "Sellcom", "position": "Linux Support (2024 - Present)", "duties": \
         "- Working as a 2nd level support for BBVA' servers which use SUSE OS and Ubuntu.\
            \n- Solving problems about services, periferial devices and some infreastructure issues.\
            \n- Managing dns's and ip's under Infoblox system.\
            \n- Validating logs and SO uptdates in all BBVA Bank branches in Mexico.\
            \n- Monitoring every server alert using OBM and solving incidents with \
            Service Now and Jira"},

        {"company": "Travel Shop", "position": "Intern (2024 - 2024)", "duties": \
         "- I made a project for Operadora Travel Shop so that I could finish my undergraduate studies.\
            This project is a Desktop App which runs on Windows SO, such project is made in Python, \
            I used different libraries for gathering and treating data from their database regarding sales giving\
            the oportunity to choose specific periods of time. When the data is gathered the \
            program cleans it, then organizes the cleaned data to show it in xlsx files, finally\
            the program makes plots which display sales statistics. The program connects with the\
            enterprise's DNS server which points to the database so that employees can run the app \
            from wherever place they are."},

        {"company": "Tiendas 3B", "position": "Linux Support (2024 - 2024)", "duties": \
         "- Solving 3B store issues regarding the linux system in Ecatepc, Pachuca and Hidalgo.\
            \n- Managing tickets with Jira.\
            \n- Report making.\
            \n- Stock management.\
            \n- Installing and setting the whole cash registers' system.\
            \n- Giving infraestructure support at the 3B DC in Ecatepec."},

        {"company": "MNJ Capital", "position": "IT analyst (2023 - 2024)", "duties": \
         "- Identifying and solving system issues relating to the enterprise web page.\
            \n- Keeping in good conditions all IT manuals and software documentation.\
            \n- Working as a team to improve the whole system.\
            \n- Giving technical support"},

    ]

    return render (request, "experiences.html", {"experiences": experiences})


def certifications(request):

    certifications = [

        {"title": "Scrum Master", 
         "badge": "https://www.scrumstudy.com/certification/verify?type=SMC&number=1032526",
         "image": "images/scrum.PNG"},
        
        {"title": "Toefl ITP", "image": "images/toefl.PNG"},
        {"title": "LPIC-1", "image": "images/lpic.PNG"},
        {"title": "CCNA", "image": "images/ccna.PNG"},
        {"title": "Web Development", "image": "images/webdev.PNG"},
        {"title": "Quick Learning", "image": "images/quick.JPEG"},

    ]

    return render (request, "certifications.html", {"certifications": certifications})

def contact(request):

    return render (request, "contact.html")

def resume(request):

    resume_path="resume/emm_resume.pdf"
    
    resume_path=staticfiles_storage.path(resume_path)

    if staticfiles_storage.exists(resume_path):

        with open(resume_path, "rb") as resume_file:

            response=HttpResponse(resume_file.read(), content_type="application/pdf")

            response["Content-Disposition"]='attachment';filename='emm_resume.pdf'

            return response

    else:

        return HttpResponse("Resume not found.", status=404)