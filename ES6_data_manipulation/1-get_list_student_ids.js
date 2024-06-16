const getListStudentIds = (students) => {
    if (!Array.isArray(students)) {
        return [];
    }
    const studentids = students.map((student) => student.id);
    return studentids;
};

export default getListStudentIds;
