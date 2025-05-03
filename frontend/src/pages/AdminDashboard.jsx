import React from 'react';
import './AdminDashboard.css';

const AdminDashboard = () => {
  return (
    <div className="admin-dashboard">
      <header className="admin-header">
        <h1>Admin Dashboard</h1>
        <p>Manage your system effectively and effortlessly.</p>
      </header>

      <section className="stats-section">
        <div className="stat-card">
          <h2>Total Courses</h2>
          <p>128</p>
        </div>
        <div className="stat-card">
          <h2>Registered Users</h2>
          <p>502</p>
        </div>
        <div className="stat-card">
          <h2>Pending Requests</h2>
          <p>12</p>
        </div>
      </section>

      <section className="nav-section">
        {[
          { title: 'Manage Courses', link: '/admin/courses' },
          { title: 'Manage Users', link: '/admin/users' },
          { title: 'Upload CSV', link: '/admin/upload' },
          { title: 'Reports & Analytics', link: '/admin/reports' },
          { title: 'Settings', link: '/admin/settings' },
        ].map((item, i) => (
          <a href={item.link} key={i} className="nav-card">
            <h3>{item.title}</h3>
            <p>Click to view</p>
          </a>
        ))}
      </section>
    </div>
  );
};

export default AdminDashboard;
