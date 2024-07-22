"use client";

import { Loading } from "@/components/Loading";
import StatCard from "@/components/StatCard";
import { AppointmentTable } from "@/components/appointments";

import { useProjectStore } from "@/hooks/useProjectStore";
import Image from "next/image";
import Link from "next/link";
import { useEffect } from "react";

const Admin = () => {
  const { appointments, appointmentsLoading, getAppointments, fetchDoctors } =
    useProjectStore();

  useEffect(() => {
    getAppointments();
    fetchDoctors();
  }, []);

  return (
    <div className="mx-auto flex max-w-7xl flex-col space-y-14">
      <header className="admin-header">
        <Link href="/" className="cursor-pointer">
          <Image
            src="logo.svg"
            width={32}
            height={32}
            alt="Logo"
            className="h-8 w-fit"
          />
        </Link>
        <p className="text-16-semibold">Admin Dashboard</p>
      </header>
      <main className="admin-main">
        <section className="w-full space-y-4">
          <h1 className="header">Welcome Back!</h1>
          <p className="text-dark-700">
            Start the day with managing new appointments
          </p>
        </section>

        {appointmentsLoading ? (
          <Loading />
        ) : (
          appointments && (
            <>
              <section className="admin-stat">
                <StatCard type="schedule" count={appointments.scheduledCount} />
                <StatCard type="create" count={appointments.pendingCount} />
                <StatCard type="cancel" count={appointments.cancelledCount} />
              </section>

              <section>
                <AppointmentTable data={appointments.appointments} />
              </section>
            </>
          )
        )}
      </main>
    </div>
  );
};

export default Admin;
