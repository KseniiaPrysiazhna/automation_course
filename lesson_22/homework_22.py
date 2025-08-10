import random
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Table,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session

Base = declarative_base()

student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship("Course", secondary=student_course, back_populates="students")

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}')"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)

    students = relationship("Student", secondary=student_course, back_populates="courses")

    def __repr__(self):
        return f"Course(id={self.id}, title='{self.title}')"

def get_student_or_raise(session: Session, student_id: int) -> Student:
    student = session.query(Student).get(student_id)
    if not student:
        raise ValueError(f"Student with id={student_id} not found")
    return student

def get_course_or_raise(session: Session, course_id: int) -> Course:
    course = session.query(Course).get(course_id)
    if not course:
        raise ValueError(f"Course with id={course_id} not found")
    return course

def initialize_database(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def seed_data(session: Session):
    course_titles = [
        "Math",
        "Programming",
        "Physics",
        "History",
        "English",
    ]
    courses = [Course(title=t) for t in course_titles]
    session.add_all(courses)
    session.flush()

    first_names = [
        "Andrii", "Bohdan", "Viktoriia", "Hanna", "Dmytro", "Eva", "Kateryna", "Vlad",
        "Iryna", "Kostiantyn", "Liudmyla", "Mykhailo", "Nataliia", "Oleksandr", "Petro",
        "Roman", "Svitlana", "Taras", "Uliana", "Fedir", "Khrystyna", "Kseniia", "Mark"
    ]
    random.shuffle(first_names)
    students = [Student(name=first_names[i]) for i in range(20)]
    session.add_all(students)
    session.flush()

    for student in students:
        assigned = random.sample(courses, k=random.randint(1, 3))
        student.courses.extend(assigned)

    session.commit()

def add_student(session: Session, name: str, course_ids: list[int]):
    student = Student(name=name)
    courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
    if not courses:
        raise ValueError("No course with such id")
    student.courses.extend(courses)
    session.add(student)
    session.commit()
    print(f"Student added: {student} to {[c.title for c in courses]} course.")
    return student

def enroll_existing_student(session: Session, student_id: int, course_id: int):
    student = get_student_or_raise(session, student_id)
    course = get_course_or_raise(session, course_id)
    if course in student.courses:
        print(f"{student.name} is already in {course.title}")
        return
    student.courses.append(course)
    session.commit()
    print(f"Registred {student.name} to {course.title} course.")

def get_students_in_course(session: Session, course_id: int):
    course = get_course_or_raise(session, course_id)
    return course.students

def get_courses_of_student(session: Session, student_id: int):
    student = get_student_or_raise(session, student_id)
    return student.courses

def update_student_name(session: Session, student_id: int, new_name: str):
    student = get_student_or_raise(session, student_id)
    old = student.name
    student.name = new_name
    session.commit()
    print(f"Student name is updated from '{old}' to '{new_name}'")

def update_course_title(session: Session, course_id: int, new_title: str):
    course = get_course_or_raise(session, course_id)
    old = course.title
    course.title = new_title
    session.commit()
    print(f"Course name is updated from '{old}' to '{new_title}'")

def remove_student(session: Session, student_id: int):
    student = get_student_or_raise(session, student_id)
    session.delete(student)
    session.commit()
    print(f"Student (id={student_id}) is removed.")

def remove_student_from_course(session: Session, student_id: int, course_id: int):
    student = get_student_or_raise(session, student_id)
    course = get_course_or_raise(session, course_id)
    if course in student.courses:
        student.courses.remove(course)
        session.commit()
        print(f"Removed {student.name} from {course.title} course.")
    else:
        print(f"{student.name} was not at {course.title} course")

def main():
    engine = create_engine("sqlite:///students.db", echo=False)
    initialize_database(engine)

    session = Session(bind=engine)
    try:
        seed_data(session)

        print("\n--- Example: students at course 1 ---")
        students_course1 = get_students_in_course(session, 1)
        for s in students_course1:
            print(s)

        print("\n--- Example: student 1 courses ---")
        courses_student1 = get_courses_of_student(session, 1)
        for c in courses_student1:
            print(c)

        print("\n--- Added new student Olha to courses 2 and 3 ---")
        new_student = add_student(session, "Olha", [2, 3])

        print("\n--- Registration existed student to added course ---")
        enroll_existing_student(session, new_student.id, 4)

        print("\n--- Updating student name ---")
        update_student_name(session, new_student.id, "Olha-Mariia")

        print("\n---Update course title ---")
        update_course_title(session, 5, "English (advance)")

        print("\n--- Removing student from course ---")
        remove_student_from_course(session, new_student.id, 2)

        print("\n--- Full student removal ---")
        remove_student(session, new_student.id)

        print("\n--- Students list on course 2 ---")
        for s in get_students_in_course(session, 2):
            print(s)
    finally:
        session.close()

if __name__ == "__main__":
    main()