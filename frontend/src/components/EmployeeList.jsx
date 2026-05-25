export default function EmployeeList({ employees, onEdit, onDelete }) {
  if (!employees.length) return <p>No employees found.</p>;

  return (
    <table className="emp-table">
      <thead>
        <tr>
          <th>Name</th><th>Email</th><th>Department</th>
          <th>Role</th><th>Salary</th><th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {employees.map((emp) => (
          <tr key={emp.id}>
            <td>{emp.name}</td>
            <td>{emp.email}</td>
            <td>{emp.department}</td>
            <td>{emp.role}</td>
            <td>₹{emp.salary.toLocaleString()}</td>
            <td>
              <button onClick={() => onEdit(emp)}>Edit</button>
              <button onClick={() => onDelete(emp.id)}>Delete</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}