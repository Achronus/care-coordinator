import UserForm from "@/forms/UserForm";
import FormLayout from "@/layouts/Form";
import { DisplayImg, Logo } from "@/lib/constants";

export default function Home() {
  return (
    <main className="flex h-screen max-h-screen">
      {/* TODO: OTP Verification */}
      <FormLayout
        containerStyles="max-w-[496px] my-auto"
        logo={Logo}
        displayImg={DisplayImg}
        showAdmin
      >
        <UserForm />
      </FormLayout>
    </main>
  );
}
