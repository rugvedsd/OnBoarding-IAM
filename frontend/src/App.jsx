import { useEffect, useState } from "react";
import EmployeeForm from "./components/EmployeeForm";
import EmployeeList from "./components/EmployeeList";

const API = "http://localhost:8000/employees";

export default function App() {
  const [employees, setEmployees] = useState([]);
  const [editData, setEditData]   = useState(null);

  const fetchAll = () =>
    fetch(API).then((r) => r.json()).then(setEmployees);

  useEffect(() => { fetchAll(); }, []);

  const handleSubmit = async (data) => {
    if (editData) {
      await fetch(`${API}/${editData.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      setEditData(null);
    } else {
      await fetch(API, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
    }
    fetchAll();
  };

  const handleDelete = async (id) => {
    if (confirm("Delete this employee?")) {
      await fetch(`${API}/${id}`, { method: "DELETE" });
      fetchAll();
    }
  };

  return (
    <div className="container">
      <h1>Employee Management</h1>
      <EmployeeForm
        onSubmit={handleSubmit}
        editData={editData}
        onCancel={() => setEditData(null)}
      />
      <EmployeeList
        employees={employees}
        onEdit={setEditData}
        onDelete={handleDelete}
      />
    </div>
  );
}