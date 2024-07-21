# Care Coordinator

Care Coordinator is a demo portfolio project. Conceptually, it is a web-based appointment management software for Healthcare professionals, allowing patients to sign-up and schedule appointments with their doctor efficiently.

This full-stack application includes a host of different features on both the frontend and backend. We'll look at these in more detail in the next couple of sections.

_Note: So far, the project is about 90% complete with a few key areas to implement. Refer to the [remaining](#remaining) section for more details._

## Tech Stack

The tech stack centres around `Python` on the backend and `React.js` on the frontend.

### Backend

- [Poetry](https://python-poetry.org/) - for managing all Python packages
- [FastAPI](https://fastapi.tiangolo.com/) - for API management and database requests
- [Pydantic](https://docs.pydantic.dev/latest/) - for model/class attribute validation
- [Appwrite](https://appwrite.io/) - database management solution
- [Pytest](https://docs.pytest.org/en/8.2.x/) - for unit tests

### Frontend

- [Next.js](https://nextjs.org/) - our React.js frontend framework
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

- Uses JWT tokens for securing data between the frontend and backend
- Uses large forms with various fields and validation: inputs, email, phone, date picker, file upload, select boxes, checkboxes, textarea, etc
- Uses an OTP input to access the admin dashboard using a passcode, encrypted and stored in local storage
- Uses a data table to display appointments with actions for scheduling pending appointments or cancelling existing ones
- Users scheduling appointments receive SMS notifications

## Remaining

This section focuses on what is left to do before the project is ready for deployment (~92% complete). What's left:

- Refactor state management using [Zustand](https://docs.pmnd.rs/zustand/getting-started/introduction)
- JWT tokens
- SMS Notifications
