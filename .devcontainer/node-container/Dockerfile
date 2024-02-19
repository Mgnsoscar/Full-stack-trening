FROM node

WORKDIR /app

RUN mkdir React
RUN cd React && npx create-react-app intervju-app
RUN cd React/intervju-app && npm i axios

EXPOSE 3000

COPY ../../React/api.js ./React/intervju-app/src/api.js
COPY ../../React/App.js ./React/intervju-app/src/App.js
COPY ../../React/index.html ./React/intervju-app/public/index.html
COPY ../../React/docker-entrypoint.sh ./React

RUN chmod +x ./React/docker-entrypoint.sh
ENTRYPOINT [ "./React/docker-entrypoint.sh" ]
CMD [ "sleep", "infinity" ]
