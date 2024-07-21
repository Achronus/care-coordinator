"use client";

import { Loading } from "@/components/Loading";
import StatCard from "@/components/StatCard";
import { AppointmentTable } from "@/components/appointments";
import useFetchData from "@/hooks/useFetchData";
import { AppointmentListData } from "@/types/api";

import Image from "next/image";
import Link from "next/link";
import { useSearchParams } from "next/navigation";

const Admin = () => {
  const searchParams = useSearchParams();
  const success = searchParams.get("success") ?? false;

  const { data: appointmentData, isLoading } =
    useFetchData<AppointmentListData>("api/appointment/list", [success]);

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

        {isLoading ? (
          <Loading />
        ) : (
          appointmentData && (
            <>
              <section className="admin-stat">
                <StatCard
                  type="schedule"
                  count={appointmentData.scheduledCount}
                />
                <StatCard type="create" count={appointmentData.pendingCount} />
                <StatCard
                  type="cancel"
                  count={appointmentData.cancelledCount}
                />
              </section>

              <section>
                <AppointmentTable data={appointmentData.appointments} />
              </section>
            </>
          )
        )}
      </main>
    </div>
  );
};

export default Admin;
