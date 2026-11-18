# Этап 1: Сборка Angular
FROM node:22-alpine AS builder
WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

# Этап 2: Безопасная раздача статики через непривилегированный Nginx
FROM nginxinc/nginx-unprivileged:alpine

# Удаляем дефолтный конфиг и копируем наш
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Копируем собранный Angular из первого этапа
COPY --from=builder /app/dist/frontend/browser /usr/share/nginx/html

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
