import { cn } from "@/lib/utils";
import type { Metadata } from "next";
import { Plus_Jakarta_Sans } from "next/font/google";
import "./globals.css";

const fontSans = Plus_Jakarta_Sans({
  subsets: ["latin"],
  weight: ["300", "400", "500", "600", "700"],
  variable: "--font-sans",
});

export const metadata: Metadata = {
  title: "Your Partner in Efficient Healthcare Scheduling | CareCoordinator",
  description:
    "The ultimate solution for effortlessly managing your healthcare appointments.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={cn(`${fontSans.className} min-h-screen flex flex-col`)}>
        {children}
      </body>
    </html>
  );
}
