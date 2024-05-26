export default function createIteratorObject(report) {
  const workers = [];
  /* eslint-disable no-unused-vars */
  for (const [department, employees] of Object.entries(report.allEmployees)) {
    for (const employee of employees) {
      workers.push(employee);
    }
  }
  /* eslint-enable no-unused-vars */

  return workers;
}
