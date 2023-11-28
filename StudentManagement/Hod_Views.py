from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import *

@login_required(login_url='/')
def home(request):
    student_id=Student.objects.all().count()
    staff_id=Staff.objects.all().count()
    course_id=Course.objects.all().count()
    subject_id=Subject.objects.all().count()
    return render(request, "Hod/home.html", locals())

@login_required(login_url='/')
def Add_Student(request):
    course=Course.objects.all()
    session_year=Session_Year.objects.all()
    
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        address=request.POST.get("address")
        gender=request.POST.get("gender")
        course_id=request.POST.get("course")
        session_year_id=request.POST.get("session")
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email Already Exists")
            return redirect("Add_Student")
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Email Already Exists")
            return redirect("Add_Student")
        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=3
            )
            user.set_password(password)
            user.save()
            
            course=Course.objects.get(id=course_id)
            session_year=Session_Year.objects.get(id=session_year_id)
            
            student=Student(
                admin=user,
                gender=gender,
                address=address,
                session_year_id=session_year,
                course_id=course
            )
            student.save()
            messages.success(request, user.first_name+" "+user.last_name+" "+"are Successfully added")
            return redirect("Add_Student")
    return render(request, "Hod/add_student.html", locals())

def View_Student(request):
    students=Student.objects.all()
    print(students)
    return render(request, "Hod/view_student.html", locals())

def Edit_Student(request, id):
    student=Student.objects.filter(id=id)
    course=Course.objects.filter()
    session=Session_Year.objects.filter()
    return render(request, "Hod/edit_student.html", locals())

def Update_Student(request):
    try:
        if request.method == 'POST':
            student_id = request.POST.get('student_id')
            profile_pic = request.FILES.get('profile_pic')
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")
            address = request.POST.get("address")
            gender = request.POST.get("gender")
            course_id = request.POST.get("course")
            session_year_id = request.POST.get("session")
            
            user = CustomUser.objects.get(id=student_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            
            user.session_year_id=session_year_id
            if profile_pic!=None and profile_pic!="":
                user.profile_pic = profile_pic
            if password!=None and password!="":
                user.set_password(password)
            user.save()
            student=Student.objects.get(admin=student_id)
            student.address=address
            student.gender=gender
            course=Course.objects.get(id=course_id)
            student.course_id=course
            session=Session_Year.objects.get(id=session_year_id)
            student.session_year_id=session
            student.save()
            messages.success(request, user.first_name+" "+user.last_name+" "+"Updated Successfully")
            return redirect('View_Student')
    except:
        messages.error(request, "Error Updating Student")
        
    return render(request, "Hod/edit_student.html", locals())

def Delete_Student(request, admin):
    student=CustomUser.objects.filter(id=admin)
    student.delete()
    messages.success(request, "User Record Successfully Deleted")
    return redirect('View_Student')

def Add_Course(request):
    if request.method == 'POST':
        course_name=request.POST.get("course")
        course=Course(name=course_name)
        course.save()
    return render(request, "Hod/add_course.html", locals())

def View_Course(request):
    course=Course.objects.all()
    return render(request, "Hod/view_course.html", locals())

def Edit_Course(request,id):
    course=Course.objects.filter(id=id)
    return render(request, "Hod/edit_course.html", locals())

def Update_Course(request):
    try:
        if request.method == 'POST':
            course_id=request.POST.get("course_id")
            course_name=request.POST.get("course_name")
            course=Course.objects.get(id=course_id)
            course.name=course_name
            course.save()
            messages.success(request, "Course Edited Successfully.")
            return redirect("View_Course")
    except:
        messages.error(request, "Error Updating Course.") 
    return render(request, "Hod/edit_course.html", locals())

def Delete_Course(request, id):
    course=Course.objects.get(id=id)
    course.delete()
    messages.success(request, "Course Deleted Successfully.")
    return redirect('View_Course')


def Add_Staff(request):
    if request.method == 'POST':
        profile_pic=request.FILES.get("profile_pic")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "Email Already Exists")
            return redirect("Add_Staff")
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Email Already Exists")
            return redirect("Add_Staff")
        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                profile_pic=profile_pic,
                user_type=2
            )
            user.set_password(password)
            user.save()
            staff=Staff(
                admin=user,
                gender=gender,
                address=address,
            )
            staff.save()
            messages.success(request, user.first_name+" "+user.last_name+" "+"are Successfully added")
            return redirect("Add_Staff")
    return render(request, "Hod/add_staff.html", locals())

def View_Staff(request):
    staff=Staff.objects.all()
    return render(request, "Hod/view_staff.html", locals())

def Edit_Staff(request,id):
    staff=Staff.objects.filter(id=id)
    return render(request, "Hod/edit_staff.html", locals())

def Update_Staff(request):
    try:
        if request.method == 'POST':
            staff_id = request.POST.get('staff_id')
            profile_pic = request.FILES.get('profile_pic')
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")
            username = request.POST.get("username")
            password = request.POST.get("password")
            address = request.POST.get("address")
            gender = request.POST.get("gender")
            
            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            
            if profile_pic!=None and profile_pic!="":
                user.profile_pic = profile_pic
            if password!=None and password!="":
                user.set_password(password)
            user.save()
            
            staff=Staff.objects.get(admin=staff_id)
            staff.address=address
            staff.gender=gender
            staff.save()
            messages.success(request, "Staff Edited Successfully.")
            return redirect("View_Staff")
    except:
        messages.error(request, "Staff Edited Failed")
        return redirect("View_Staff")
            
def Delete_Staff(request, admin):
    staff=CustomUser.objects.filter(id=admin)
    staff.delete()
    messages.success(request, "Staff Deleted Successfully.")
    return redirect('View_Staff')

def Add_Subject(request):
    course=Course.objects.all()
    staff=Staff.objects.all()
    if request.method == 'POST':
        subject_name=request.POST.get('name')
        course_id=request.POST.get('course')
        staff_id=request.POST.get('staff')
        if Subject.objects.filter(name=subject_name).exists():
            messages.warning(request, "Subject Already Exists")
        else:
            course=Course.objects.get(id=course_id)
            staff=Staff.objects.get(id=staff_id)
            subject=Subject(name=subject_name, course=course, staff=staff)
            subject.save()
            messages.success(request, subject_name+" Subject Added")
            return redirect("Add_Subject")
    return render(request, "Hod/add_subject.html", locals())

def View_Subject(request):
    subject=Subject.objects.all()
    return render(request, "Hod/view_subject.html", locals())

def Edit_Subject(request, id):
    subject=Subject.objects.get(id=id)
    course=Course.objects.all()
    staff=Staff.objects.all()
    return render(request, "Hod/edit_subject.html", locals())

def Update_Subject(request):
    try:
        if request.method=='POST':
            subject_id=request.POST.get("subject_id")
            subject_name=request.POST.get("subject")
            course_id=request.POST.get("course")
            staff_id=request.POST.get("staff")
            course=Course.objects.get(id=course_id)
            staff=Staff.objects.get(id=staff_id)
            
            subject=Subject(id=subject_id, name=subject_name, course=course, staff=staff)
            subject.save()
            messages.success(request, subject_name+" Successfully Added.")
            return redirect("View_Subject")
    except:
        messages.error(request, "error updating subject")
        return redirect("View_Subject")
        
def Delete_Subject(request, id):
    subject=Subject.objects.filter(id=id)
    subject.delete()
    return redirect('View_Subject')

def Add_Session(request):
    if request.method=='POST':
        s_session=request.POST.get('session_start')
        e_session=request.POST.get('session_end')
        if Session_Year.objects.filter(session_start=s_session, session_end=e_session).exists():
            messages.warning(request, "Already exists")
        else:
            session=Session_Year(session_start=s_session, session_end=e_session)
            session.save()
            return redirect("Add_Session")
    return render(request, "Hod/add_session.html", locals())

def View_Session(request):
    session=Session_Year.objects.all()
    return render(request, "Hod/view_session.html", locals())
    
def Edit_Session(request, id):
    session=Session_Year.objects.get(id=id)
    return render(request, "Hod/edit_session.html", locals())
    
def Update_Session(request):
    try:
        if request.method=='POST':
            session_id=request.POST.get('session_id')
            s_session=request.POST.get('session_start')
            e_session=request.POST.get('session_end')
            
            session=Session_Year.objects.get(id=session_id)
            session.session_start=s_session
            session.session_end=e_session
            session.save()
            messages.success(request, "Session successfully Updated")
            return redirect("View_Session")
    except:
        messages.error(request, "Failed to add session")
        return redirect("View_Session")

def Delete_Session(request, id):
    session=Session_Year.objects.filter(id=id)
    session.delete()
    messages.success(request, "Successfully deleted")
    return redirect("View_Session")

def Staff_Send_Notification(request):
    staff=Staff.objects.all()
    see_notification=Staff_Notification.objects.all()
    return render(request, 'Hod/staff_notification.html', locals())

def Staff_Save_Notification(request):
    if request.method == 'POST':
        msg=request.POST.get('message')
        staff_id=request.POST.get('staff_id')
        staff=Staff.objects.get(admin=staff_id)
        s_notification=Staff_Notification(staff_id=staff,message=msg)
        s_notification.save()
        messages.success(request, "Notification Sended.")
        return redirect('Staff_Send_Notification')
    else:
        messages.success(request, "Notification Failed.")
        return redirect('Staff_Send_Notification')

def Staff_Leave_View(request):
    leave=Staff_Leave.objects.all()
    return render(request, 'Hod/view_staff_leave.html', locals())

def Staff_Leave_Approve(request, id):
    leave=Staff_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('Staff_Leave_View')

def Staff_Leave_Reject(request, id):
    leave=Staff_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('Staff_Leave_View')

def Staff_Feedback_View(request):
    staff_feedback=Staff_Feedback.objects.all()
    return render(request, 'Hod/view_staff_feedback.html', locals())

def Staff_Feedback_Reply(request):
    if request.method == 'POST':
        staff_id=request.POST.get('staff_id')
        reply=request.POST.get('reply')
        feedback=Staff_Feedback.objects.get(staff_id=staff_id)
        feedback.feedbackreply=reply
        feedback.save()
        return redirect('Staff_Feedback_View')

def View_Attendance(request):
    subject=Subject.objects.all()
    session_year=Session_Year.objects.all()
    action=request.GET.get('action')
    get_subject=None
    get_session_year=None
    attendance_date=None
    attendance_report=None
    if action is not None:
        if request.method == 'POST':
            subject_id=request.POST.get('subject_id')
            session_year_id=request.POST.get('session_year_id')
            attendance_date=request.POST.get('attendance_date')
            
            get_subject=Subject.objects.get(id=subject_id)
            get_session_year=Session_Year.objects.get(id=session_year_id)
            attendancee=Attendance.objects.filter(subject_id=get_subject, session_year_id=get_session_year, attendance_date=attendance_date)
            for i in attendancee:
                attendance_id=i.id
                attendance_report=Attendance_Report.objects.filter(attendance=attendance_id)
    
    return render(request, 'Hod/view_attendance.html', locals())

def Student_Send_Notification(request):
    student=Student.objects.all()
    see_notification=Student_Notification.objects.all()
    return render(request, 'Hod/student_notification.html', locals())

def Student_Save_Notification(request):
    if request.method == 'POST':
        msg=request.POST.get('message')
        student_id=request.POST.get('student_id')
        student=Student.objects.get(admin=student_id)
        s_notification=Student_Notification(student_id=student,message=msg)
        s_notification.save()
        messages.success(request, "Notification Sended.")
        return redirect('Student_Send_Notification')
    else:
        messages.success(request, "Notification Failed.")
        return redirect('Student_Send_Notification')
    
def Student_Leave_View(request):
    leave=Student_Leave.objects.all()
    return render(request, 'Hod/view_student_leave.html', locals())

def Student_Leave_Approve(request, id):
    leave=Student_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('Student_Leave_View')

def Student_Leave_Reject(request, id):
    leave=Student_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('Student_Leave_View')

def Student_Feedback_View(request):
    student_feedback=Student_Feedback.objects.all()
    return render(request, 'Hod/view_student_feedback.html', locals())

def Student_Feedback_Reply(request):
    if request.method == 'POST':
        student_id=request.POST.get('student_id')
        reply=request.POST.get('reply')
        feedback=Student_Feedback.objects.get(student_id=student_id)
        feedback.feedbackreply=reply
        feedback.save()
        return redirect('Student_Feedback_View')