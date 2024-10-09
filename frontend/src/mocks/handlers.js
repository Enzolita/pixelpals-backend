import { rest } from "msw";

const baseURL = "https://pixelpals-backend-49bb71efec81.herokuapp.com/";

export const handlers = [
  rest.get(`${baseURL}dj-rest-auth/user/`, (req, res, ctx) => {
    return res(
      ctx.json({
        pk: 3,
        username: "Elenita",
        email: "",
        first_name: "",
        last_name: "",
        profile_id: 3,
        profile_image:
          "https://res.cloudinary.com/dqk6ad4tr/image/upload/v1/media/images/Sk%C3%A4rmbild_2024-10-03_003509_j804sz",
      })
    );
  }),
  rest.post(`${baseURL}dj-rest-auth/logout/`, (req, res, ctx) => {
    return res(ctx.status(200));
  }),
];