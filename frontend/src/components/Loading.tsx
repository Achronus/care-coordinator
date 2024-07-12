import Image from "next/image";

export const Loading = () => {
  return (
    <section className="remove-scrollbar container my-auto">
      <Image
        src="/icons/loader.svg"
        width={100}
        height={100}
        alt="Loader"
        className="animate-spin mb-12 h-10 w-fit"
      />
    </section>
  );
};
