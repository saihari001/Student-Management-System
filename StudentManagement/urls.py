"""
URL configuration for StudentManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from  .import views,Hod_Views,Staff_Views,Student_Views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='BASE'),
    path('', views.Login, name='Login'),
    path('Hod/home', Hod_Views.home, name='hod_home'),
    path('logout', views.Logout, name="Logout"),
    path('profile', views.Profile, name='Profile'),
    path('profile_update', views.Profile_Update, name='Profile_Update'),
    path('Hod/Course/Add', Hod_Views.Add_Course, name='Add_Course'),
    path('Hod/Course/View', Hod_Views.View_Course, name='View_Course'),
    path('Hod/Course/Edit/<int:id>', Hod_Views.Edit_Course, name='Edit_Course'),
    path('Hod/Course/Update', Hod_Views.Update_Course, name='Update_Course'),
    path('Hod/Course/Delete/<int:id>', Hod_Views.Delete_Course, name='Delete_Course'),
    path('Hod/Subject/Add', Hod_Views.Add_Subject, name='Add_Subject'),
    path('Hod/Subject/View', Hod_Views.View_Subject, name='View_Subject'),
    path('Hod/Subject/Edit/<int:id>', Hod_Views.Edit_Subject, name='Edit_Subject'),
    path('Hod/Subject/Update', Hod_Views.Update_Subject, name='Update_Subject'),
    path('Hod/Subject/Delete/<str:admin>', Hod_Views.Delete_Subject,name='Delete_Subject'),
    path('Hod/Session/Add', Hod_Views.Add_Session, name='Add_Session'),
    path('Hod/Session/View', Hod_Views.View_Session, name='View_Session'),
    path('Hod/Session/Edit/<int:id>', Hod_Views.Edit_Session, name='Edit_Session'),
    path('Hod/Session/Update', Hod_Views.Update_Session, name='Update_Session'),
    path('Hod/Session/Delete/<int:id>', Hod_Views.Delete_Session,name='Delete_Session'),
    
    #Staff views.
    path('Hod/Staff/Add', Hod_Views.Add_Staff, name='Add_Staff'),
    path('Hod/Staff/View', Hod_Views.View_Staff, name='View_Staff'),
    path('Hod/Staff/Edit/<int:id>', Hod_Views.Edit_Staff, name='Edit_Staff'),
    path('Hod/Staff/Update', Hod_Views.Update_Staff, name='Update_Staff'),
    path('Hod/Staff/Delete/<str:admin>', Hod_Views.Delete_Staff, name='Delete_Staff'),
    path('Hod/Staff/Send_Notification', Hod_Views.Staff_Send_Notification,name='Staff_Send_Notification'),
    path('Hod/Staff/Save_Notification', Hod_Views.Staff_Save_Notification,name='Staff_Save_Notification'),
    path('Hod/Staff/Leave/View', Hod_Views.Staff_Leave_View,name='Staff_Leave_View'),
    path('Hod/Staff/Leave/Approve/<int:id>', Hod_Views.Staff_Leave_Approve,name='Staff_Leave_Approve'),
    path('Hod/Staff/Leave/Reject/<int:id>', Hod_Views.Staff_Leave_Reject,name='Staff_Leave_Reject'),
    path('Hod/Staff/Feedback_View', Hod_Views.Staff_Feedback_View, name='Staff_Feedback_View'),
    path('Hod/Staff/Feedback_Reply', Hod_Views.Staff_Feedback_Reply, name='Staff_Feedback_Reply'),
    path('Hod/View_Attendance', Hod_Views.View_Attendance, name='View_Attendance'),
    
    #Student views.
    path('Hod/Student/Add', Hod_Views.Add_Student, name='Add_Student'),
    path('Hod/Student/View', Hod_Views.View_Student, name='View_Student'),
    path('Hod/Student/Edit/<int:id>', Hod_Views.Edit_Student, name='Edit_Student'),
    path('Hod/Student/Update', Hod_Views.Update_Student, name='Update_Student'),
    path('Hod/Student/Delete/<str:admin>', Hod_Views.Delete_Student, name='Delete_Student'),
    path('Hod/Student/Send_Notification', Hod_Views.Student_Send_Notification,name='Student_Send_Notification'),
    path('Hod/Student/Save_Notification', Hod_Views.Student_Save_Notification,name='Student_Save_Notification'),
    path('Hod/Student/Leave/View', Hod_Views.Student_Leave_View,name='Student_Leave_View'),
    path('Hod/Student/Leave/Approve/<int:id>', Hod_Views.Student_Leave_Approve,name='Student_Leave_Approve'),
    path('Hod/Student/Leave/Reject/<int:id>', Hod_Views.Student_Leave_Reject,name='Student_Leave_Reject'),
    path('Hod/Student/Feedback_View', Hod_Views.Student_Feedback_View, name='Student_Feedback_View'),
    path('Hod/Student/Feedback_Reply', Hod_Views.Student_Feedback_Reply, name='Student_Feedback_Reply'),


    



    
    
    
    #Staff
    path('Staff/Home', Staff_Views.Home, name='Staff_Home'),
    path('Staff/Notification', Staff_Views.Staff_View_Notification,name='Staff_View_Notification'),
    path('Staff/Notification_mark_as_done/<str:status>', Staff_Views.Staff_View_Notification_mark_as_done,name='Staff_View_Notification_mark_as_done'),
    path('Staff/ApplyForLeave', Staff_Views.Apply_For_Leave, name='Staff_Leave'),
    path('Staff/ApplyForLeaveSave', Staff_Views.Apply_For_Leave_Save, name='Staff_Leave_Save'),
    path('Staff/Feedback', Staff_Views.Staff_Apply_Feedback, name='Staff_Feedback'),
    path('Staff,FeedbackSave', Staff_Views.Staff_Apply_Feedback_Save, name='Staff_Feedback_Save'),
    path('Staff/Take_Attendance', Staff_Views.Staff_Take_Attendance, name='Staff_Take_Attendance'),
    path('Staff/Save_Attendance', Staff_Views.Staff_Save_Attendance, name='Staff_Save_Attendance'),
    path('Staff/View_Attendance', Staff_Views.Staff_View_Attendance, name='Staff_View_Attendance'),
    path('Staff/Student_Result', Staff_Views.Student_Result, name='Student_Result'),
    path('Staff/Student_Result_Save', Staff_Views.Student_Result_Save,name='Student_Result_Save'),

    #Student
    path('Student/Home', Student_Views.Home, name='Student_Home'),
    path('Student/Result', Student_Views.View_Result, name='View_Result'),
    path('Student/Notification', Student_Views.Student_View_Notification,name='Student_View_Notification'),
    path('Student/Notification_mark_as_done/<str:status>', Student_Views.Student_View_Notification_mark_as_done,name='Student_View_Notification_mark_as_done'),
    path('Student/ApplyForLeave', Student_Views.Student_Apply_For_Leave, name='Student_Leave'),
    path('Student/ApplyForLeaveSave', Student_Views.Student_Apply_For_Leave_Save, name='Student_Leave_Save'),
    path('Student/Feedback', Student_Views.Student_Apply_Feedback, name='Student_Feedback'),
    path('Student,FeedbackSave', Student_Views.Student_Apply_Feedback_Save, name='Student_Feedback_Save'),
    # path('Student/View_Attendance', Student_Views.Student_View_Attendance, name='Student_View_Attendance'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
