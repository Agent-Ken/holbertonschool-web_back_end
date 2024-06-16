const getStudentIdsSum = (students) => {
  const sum = students.reduce((all, next) => all + next.id, 0);
  return sum;
};

export default getStudentIdsSum;
