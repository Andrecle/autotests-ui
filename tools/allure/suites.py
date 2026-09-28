from enum import Enum


class AllureSuite(str, Enum):
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    AUTHENTICATION = "Authentication"


class AllureParentSuite(str,Enum):
    LMS = "LMS system"
    STUDENT = "Student system"
    ADMINISTRATION = "Administration system"

class AllureSubSuite(str,Enum):
    COURSES = "Courses"
    DASHBOARD = "Dashboard"
    REGISTRATION = "Registration"
    AUTHORIZATION = "Authorization"