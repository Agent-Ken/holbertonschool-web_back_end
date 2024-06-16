const updateStudentGradeByCity = (students, city, newGrades) => {
  if (!Array.isArray(students) || !Array.isArray(newGrades)) {
    return [];
  }

  const studentByCity = students
    .filter((student) => student.location === city)
    .map((student) => {
      const studentGrade = newGrades.filter((note) => student.id === note.studentId);
      let grade = 'N/A';

      if (studentGrade[0]) {
        grade = studentGrade[0].grade;
      }

      return { ...student, grade };
    });

  return studentByCity;
};

export default updateStudentGradeByCity;
