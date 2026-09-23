class Grade:
    def __init__(self, stu_id: int, crc_code: int, score: float) -> None:
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:

    def set_file(self, address: str) -> None:
        self.address = address

    def load(self, line_number: int) -> Grade:
        with open(self.address, "r") as f:
            lines = f.readlines()

        if len(lines) < line_number:
            return None

        datas = lines[line_number - 1].split()

        grade_object = Grade(
            int(datas[0]),
            int(datas[1]),
            float(datas[2])
        )

        return grade_object

    def calc_student_average(self, student_id: int) -> float:
        total = 0
        number = 0

        for i in range(1, self.count() + 1):
            grade = self.load(i)

            if grade.student_id == student_id:
                total += grade.score
                number += 1

        return total / number

    def calc_course_average(self, course_code: int) -> float:
        total = 0
        number = 0

        for i in range(1, self.count() + 1):
            grade = self.load(i)

            if grade.course_code == course_code:
                total += grade.score
                number += 1

        return total / number

    def count(self) -> int:
        with open(self.address, "r") as f:
            lines = f.readlines()

        return len(lines)

    def save(self, grade: Grade) -> None:
        for i in range(1, self.count() + 1):
            old_grade = self.load(i)

            if old_grade.student_id == grade.student_id and old_grade.course_code == grade.course_code:
                return

        with open(self.address, "a") as f:
            if self.count() > 0:
                f.write("\n")

            f.write(f"{grade.student_id} {grade.course_code} {grade.score}")