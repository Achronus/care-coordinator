_This branch contains files for the `frontend` demo mode_

# Care Coordinator - Demo Project

Care Coordinator is one of my demo portfolio projects. Conceptually, it is a web-based appointment management software for Healthcare professionals, allowing patients to sign-up and schedule appointments with their doctor efficiently.

This full-stack application includes a host of different features on both the frontend and backend. We'll look at these in more detail in the next section.

## A Note On Code

As a demo application, all the `backend` endpoints are set into `demo` mode. This means the responses don't connect directly to the database, instead they display data that looks like the response. 

Similarly, the `frontend` forms are mostly disabled. You can select some for interactive purposes. Form validation has been disabled and you cannot add or update any records in the database.

To view the code without `demo_mode`, check the [no-demo-mode](https://github.com/Achronus/care-coordinator/tree/no-demo-mode) branch.

## Tech Stack

The tech stack centres around `Python` on the backend and `Next.js` on the frontend.

### Backend

- [Poetry](https://python-poetry.org/) - for managing all Python packages
- [FastAPI](https://fastapi.tiangolo.com/) - for API management and database requests
- [Pydantic](https://docs.pydantic.dev/latest/) - for model/class attribute validation
- [Appwrite](https://appwrite.io/) - database management solution

### Frontend

- [Next.js](https://nextjs.org/) - our React.js frontend framework
- [Zustand](https://docs.pmnd.rs/zustand/getting-started/introduction) - for global data state management
- [Zod](https://zod.dev/) - for form validation
- [Shadcn/ui](https://ui.shadcn.com/) - for building our components
- [Typescript](https://www.typescriptlang.org/) - for prop type safety and validation
- [Lucide React](https://lucide.dev/) - for lightweight and beautiful icons
- [TailwindCSS](https://tailwindcss.com/) - for CSS styling

### Notable Features

- Uses Python generics for consistent route reponses

    1. Success response example:
    ```json
    {
        "status": "success",
        "code": 200,
        "response": "200_OK",
        "data": {
            "API": "route data",
        },
        "headers": {
            "optional": "response headers",
        }
    }
    ```

    2. Error response example:
    ```json
    {
        "status": "error",
        "code": 404,
        "response": "404_NOT_FOUND",
        "message": "User does not exist.",
        "headers": {
            "optional": "response headers",
        }
    }
    ```

- Uses large forms with various fields and validation: inputs, email, phone, date picker, file upload, select boxes, checkboxes, textarea, etc
- Uses an OTP input to access the admin dashboard using a passcode, encrypted and stored in local storage
- Uses a data table to display appointments with actions for scheduling pending appointments or cancelling existing ones

## Extensions

While the tool is complete, there are some noteworthy extensions that could be added:

- Patient appointment management - a login portal for patient's so they can manage their own appointments
- SMS notifications - appointment notifications sent to a patients mobile device with information about their upcoming appointments
