"use client";

import { Loading } from "@/components/Loading";
import StatCard from "@/components/StatCard";
import useGetApiData from "@/hooks/useGetApiData";
import { AppointmentListData } from "@/types/api";

import Image from "next/image";
import Link from "next/link";

const Admin = () => {
  const {
    data: appointmentData,
    isLoading,
    error,
  } = useGetApiData<AppointmentListData>("api/appointment/list");

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
            <section className="admin-stat">
              <StatCard
                type="schedule"
                count={appointmentData.scheduledCount}
              />
              <StatCard type="create" count={appointmentData.pendingCount} />
              <StatCard type="cancel" count={appointmentData.cancelledCount} />
            </section>
          )
        )}
      </main>
    </div>
  );
};

export default Admin;
