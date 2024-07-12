import { cn } from "@/lib/utils";
import Image from "next/image";
import Link from "next/link";

type Props = {
  containerStyles: string;
  logo: ImageType;
  displayImg: ImageType;
  children: React.ReactNode;
};

const FormLayout = ({ containerStyles, logo, displayImg, children }: Props) => {
  return (
    <>
      <section className="remove-scrollbar container my-auto">
        <div className={cn("sub-container", containerStyles)}>
          <Image
            src={logo.src}
            height={logo.height}
            width={logo.width}
            alt={logo.alt}
            className={cn("mb-12 h-10 w-fit", logo.className ?? "")}
          />
          {/* Form */}
          {children}

          {/* Footer */}
          <div className="text-14-regular mt-20 flex justify-between">
            <div>
              <p className="copyright">&copy; 2024 CareCoordinator</p>
              <Link href="https://www.flaticon.com/free-icons/healthcare-and-medical">
                <p className={cn("copyright", "!text-xs mt-2")}>
                  Logo by{" "}
                  <span className="underline hover:opacity-80 transition-all">
                    Flaticon
                  </span>
                </p>
              </Link>
            </div>
            <Link href="/?admin=true" className="text-green-500">
              Admin
            </Link>
          </div>
        </div>
      </section>

      <Image
        src={displayImg.src}
        height={displayImg.height}
        width={displayImg.width}
        alt={displayImg.alt}
        className={cn("side-img", displayImg.className ?? "")}
      />
    </>
  );
};

export default FormLayout;
