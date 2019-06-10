import os
from datetime import datetime
# from reportlab.pdfgen import canvas
# from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from ravibasics.functions.functions import handle_uploaded_file
# from ravibasics.functions.universityxlscreator2 import CREATEXLSFROMPDF
# from ravibasics.functions.UniversityPdftoXLS import CREATEXLSFROMPDF
# from ravibasics.forms import UploadFiles
from ravibasics.functions.UinversityAlgorithmConvertXLS3 import CREATEXLSFROMPDF
# Create your views here.


def index(req):
    now = datetime.now().date()
    time = datetime.now().time()
    downloadpath = ''
    if req.method == "POST":
        print('Index Form Data = ', req.POST)
        print('Index Form File Data = ', req.FILES)
        FileName = req.FILES['updf']
        print('Index Form File Input of write stream = ', FileName)
        handle_uploaded_file(FileName)
        print('done...')
        InputPath = os.getcwd()+'/ravibasics/static/upload/'+str(FileName)
        print('Your Input path file = ', InputPath)
        ans = CREATEXLSFROMPDF(InputPath)
        print('XLS path = ', ans)
        FileName = str(FileName)
        # downloadpath = str('../../'+FileName[:-4]+'.xls')
        # downloadpath = str(os.getcwd()+'/ravibasics/static/output/'+FileName[:-4]+'.xls'+'')
        # downloadpath = str(ans)
        # downloadpath = str('../static/output/'+FileName[:-4]+'.xls')
        downloadpath = str('../static/output/'+ans)
        print('New DownloadPath = ', downloadpath)
        # response = HttpResponse(conn)
        # FuploadPDF = UploadFiles(req.POST,req.FILES)
        # if FuploadPDF.is_valid():
        #     handle_uploaded_file(req.FILES['FuploadPDF'])
        #     return HttpResponse("File uploaded Successfully...")
    else:
        print('Your method is not POST....')
        # FuploadPDF = UploadFiles()

    return render(req, 'index.html', {'today': now, 'time': time, 'downloadpath': downloadpath})
    # return HttpResponse('<h1>In Index...</h1>')
# def contact(req):
#     phno = '9821960726'
#     return render(req,'contact.html',{'contact':phno})
#     # return HttpResponse('<h1>In Contact...</h1>')
# def login(req):
#     return render(req,'login.html')


# def loginresponse(req):
#     username =''
#     pdfpathI=''
#     xlspathI=''
#     pdferror=''
#     xlserror=''
#     errors=[]
#     print('req = ',req)
#     print('req POST = ',req.POST)
#     if 'username' in req.POST and 'ipupdf' in req.POST and 'idxls' in req.POST and 'password' in req.POST :
#         username = req.POST['username']
#         print('USERNAME  = ',username)
#         pdfpathI= req.POST['ipupdf']
#         xlspathI= req.POST['idxls']
#         print('PDFI = ',pdfpathI,'XLSI = ',xlspathI)
#         if(pdfpathI.find('.pdf')>-1):
#             pdfpathI =os.getcwd()+'/'+pdfpathI
#             print('New Updated = ',pdfpathI)
#             print("REAL PATH = ",os.path.dirname(os.path.realpath(__file__)))
#         else:
#             print('not conains .pdf..')
#             pdferror= 'File type must be .PDF/.pdf'
#         if(xlspathI.find('.xls')>-1):
#             xlspathI =os.getcwd()+'/'+xlspathI
#             print("REAL PATH = ",os.path.dirname(os.path.realpath(__file__)))
#         else:
#             print('not contains .xls....')
#             xlserror= 'File type must be .XLS/.xls'
#         if not username:
#             errors.append("Please Fill this field")
#         elif len(username)<10:
#             errors.append("Should be Greater then 10")
#         else:
#             print('USERNAME = ',username)
#             return render(req,'loginresponse.html',{'username':username})

#         return render(req,'login.html',{'errors':errors,'pdferror':pdferror,'xlserror':xlserror})
#     # return render(req,'loginresponse.html')

# def loginValidate(req):
#     errors=[]
#     print('In Login Validate ....')
#     if 'password' in req.POST:
#         password = req.POST['password']
#         print('Password = ',password)
#         if(password == ''):
#             errors.append("This field can not be empty..")
#         elif(len(password)<10):
#             errors.append("Password can not be less then 10 ")
#         return JsonResponse(errors,safe=False)
