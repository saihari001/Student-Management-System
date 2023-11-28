from django.shortcuts import redirect
from django.shortcuts import redirect, render
from django.contrib import messages
from app.models import *

def Home(request):
    return render(request, 'student/home.html', locals())

def View_Result(request):
    student=Student.objects.get(admin=request.user.id)
    result=Add_Result.objects.filter(student=student)
    for i in result:
        assignment_mark=i.assignment_mark
        exam_mark=i.exam_mark
        marks=((assignment_mark+exam_mark)/2)
    return render(request, 'Student/view_result.html', locals())

def Student_View_Notification(request):
    student=Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id=i.id
        message=Student_Notification.objects.filter(student_id=student_id)
    return render(request, 'Student/notification.html', locals())

def Student_View_Notification_mark_as_done(request,status):
    notification=Student_Notification.objects.get(id=status)
    notification.status=1
    notification.save()
    messages.success(request, "Marked as Done.")
    return redirect("Student_View_Notification")

def Student_Apply_For_Leave(request):
    student=Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id=i.id
        student_leave=Student_Leave.objects.filter(student_id=student_id)
    return render(request, 'Student/leave.html', locals())

def Student_Apply_For_Leave_Save(request):
    if request.method == 'POST':
        leave_date=request.POST.get('leave_date')
        leave_reason=request.POST.get('leave_reason')
        student=Student.objects.get(admin=request.user.id)
        leave=Student_Leave(student_id=student, date=leave_date, message=leave_reason)
        leave.save()
        messages.success(request, "Leave Request Submitted")
        return redirect('Student_Leave')
    
def Student_Apply_Feedback(request):   
    student=Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id=i.id
        student_feedback=Student_Feedback.objects.filter(student_id=student_id)   
    return render(request, 'Student/feedback.html', locals())

def Student_Apply_Feedback_Save(request):
    if request.method=='POST':
        feedback=request.POST.get('feedback')
        student=Student.objects.get(admin=request.user.id)
        feedback=Student_Feedback(student_id=student, feedback=feedback, feedbackreply="")
        feedback.save()
        messages.success(request, "feedback successfully sended")
        return redirect('Student_Feedback')