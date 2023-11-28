from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import *

def Home(request):
    return render(request, 'staff/home.html', locals())

def Staff_View_Notification(request):
    staff=Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id=i.id
    message=Staff_Notification.objects.filter(staff_id=staff_id)
    return render(request, 'Staff/notification.html', locals())

def Staff_View_Notification_mark_as_done(request,status):
    notification=Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    messages.success(request,"Marked as done.")
    return redirect('Staff_View_Notification')

def Apply_For_Leave(request):
    staff=Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id=i.id
        staff_leave=Staff_Leave.objects.filter(staff_id=staff_id)
    return render(request, 'Staff/leave.html', locals())

def Apply_For_Leave_Save(request):
    if request.method == 'POST':
        leave_date=request.POST.get('leave_date')
        leave_reason=request.POST.get('leave_reason')
        staff=Staff.objects.get(admin=request.user.id)
        leave=Staff_Leave(staff_id=staff, date=leave_date, message=leave_reason)
        leave.save()
        messages.success(request, "Leave Request Submitted")
        return redirect('Staff_Leave')

def Staff_Apply_Feedback(request):   
    staff=Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id=i.id
        staff_feedback=Staff_Feedback.objects.filter(staff_id=staff_id)   
    return render(request, 'Staff/feedback.html', locals())

def Staff_Apply_Feedback_Save(request):
    if request.method=='POST':
        feedback=request.POST.get('feedback')
        staff=Staff.objects.get(admin=request.user.id)
        feedback=Staff_Feedback(staff_id=staff, feedback=feedback, feedbackreply="")
        feedback.save()
        messages.success(request, "feedback successfully sended")
        return redirect('Staff_Feedback')
    
def Staff_Take_Attendance(request):
    staff_id=Staff.objects.get(admin=request.user.id)
    subject=Subject.objects.filter(staff=staff_id)
    session_year=Session_Year.objects.all()
    action=request.GET.get('action')
    get_subject=None
    get_session_year=None
    if action is not None:
        if request.method == 'POST':
            subject_id=request.POST.get('subject_id')
            session_year_id=request.POST.get('session_year_id')
            get_subject=Subject.objects.get(id=subject_id)
            get_session_year=Session_Year.objects.get(id=session_year_id)
            subject=Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id=i.course.id
                student=Student.objects.filter(course_id=student_id)
    return render(request, 'Staff/take_attendance.html', locals())

def Staff_Save_Attendance(request):
    if request.method=='POST':
        subject_id=request.POST.get('subject_id')
        session_year_id=request.POST.get('session_year_id')
        attendance_date=request.POST.get('attendance_date')
        student_id=request.POST.get('student_id')
        
        get_subject=Subject.objects.get(id=subject_id)
        get_session_year=Session_Year.objects.get(id=session_year_id)
        
        attendance=Attendance(subject_id=get_subject, session_year_id=get_session_year, attendance_date=attendance_date)
        attendance.save()
        for i in student_id:
            stud_id=i
            int_stud=int(stud_id)
            p_students=Student.objects.get(id=int_stud)
            attendance_report=Attendance_Report(student_id=p_students, attendance=attendance)
            attendance_report.save()
            return redirect('Staff_Take_Attendance')

def Staff_View_Attendance(request):
    staff=Staff.objects.get(admin=request.user.id)
    subject=Subject.objects.filter(staff_id=staff)
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
    
    return render(request, 'Staff/view_attendance.html', locals())

def Student_Result(request):
    staff=Staff.objects.get(admin=request.user.id)
    subject=Subject.objects.filter(staff=staff)
    session_year=Session_Year.objects.all()
    action=request.GET.get('action')
    get_subject=None
    get_session=None
    students=None
    if action is not None:
        if request.method=='POST':
            subject_id=request.POST.get('subject_id')
            session_year_id=request.POST.get('session_year_id')
            
            get_subject=Subject.objects.get(id = subject_id)
            get_session=Session_Year.objects.get(id = session_year_id)
            
            subjects=Subject.objects.filter(id = subject_id)
            for i in subjects:
                student_id=i.course.id
                students=Student.objects.filter(course_id=student_id, session_year_id=get_session)

    return render(request, "Staff/result.html", locals())

def Student_Result_Save(request):
    if request.method=='POST':
        subject_id=request.POST.get('subject_id')
        session_year_id=request.POST.get('session_year_id')
        student_id=request.POST.get('student_id')
        assignment_mark=request.POST.get('assignment_mark')
        exam_mark=request.POST.get('exam_mark')

        get_student=Student.objects.get(admin=student_id)
        get_subject=Subject.objects.get(id=subject_id)
        
        check_exists=Add_Result.objects.filter(student=get_student, subject=get_subject).exists()
        
        if check_exists:
            result=Add_Result.objects.get(student=get_student, subject=get_subject)
            result.assignment_mark=assignment_mark
            result.exam_mark=exam_mark
            result.save()
            messages.success(request, "Result updated Successfully")
            return redirect('Student_Result')
        else:
            student_result=Add_Result(student=get_student, subject=get_subject, assignment_mark=assignment_mark, exam_mark=exam_mark)
            student_result.save()
            messages.success(request, "Result added Successfully")
            return redirect('Student_Result')
    
    