import { useState, useEffect } from "react";

const empty = { name: "", email: "", department: "", role: "", salary: "" };

export default function EmployeeForm({ onSubmit, editData, onCancel }) {
  const [form, setForm] = useState(empty);

  useEffect(() => {
    setForm(editData || empty);
  }, [editData]);

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ ...form, salary: parseFloat(form.salary) });
    setForm(empty);
  };

  return (
    <form onSubmit={handleSubmit} className="emp-form">
      <h2>{editData ? "Edit Employee" : "Add Employee"}</h2>
      {["name", "email", "department", "role", "salary"].map((field) => (
        <input
          key={field}
          name={field}
          type={field === "salary" ? "number" : "text"}
          placeholder={field.charAt(0).toUpperCase() + field.slice(1)}
          value={form[field]}
          onChange={handleChange}
          required
        />
      ))}
      <div className="form-actions">
        <button type="submit">{editData ? "Update" : "Add"}</button>
        {editData && <button type="button" onClick={onCancel}>Cancel</button>}
      </div>
    </form>
  );
}