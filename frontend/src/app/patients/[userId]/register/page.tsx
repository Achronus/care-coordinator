"use client";

import ErrorPanel from "@/components/ErrorPanel";
import { Loading } from "@/components/Loading";
import RegisterForm from "@/forms/RegisterForm";
import useGetApiData from "@/hooks/useGetApiData";
import FormLayout from "@/layouts/Form";
import { Logo, RegisterImg } from "@/lib/constants";
import { User } from "@/types/api";

const Registration = ({ params }: { params: { userId: string } }) => {
  const {
    data: user,
    isLoading,
    error,
  } = useGetApiData<User>(`auth/user/${params.userId}`);

  return (
    <main className="flex h-screen max-h-screen">
      {isLoading ? (
        <Loading />
      ) : (
        <FormLayout
          containerStyles="max-w-[860px] h-max flex-1 flex-col py-10"
          logo={Logo}
          displayImg={RegisterImg}
        >
          {user && <RegisterForm user={user} />}
        </FormLayout>
      )}
      {error && <ErrorPanel error={error} />}
    </main>
  );
};

export default Registration;
