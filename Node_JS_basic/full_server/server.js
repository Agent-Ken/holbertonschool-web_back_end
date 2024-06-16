import express from 'express';
import controllerRouting from './routes/index';

const app = express();
const PORT = 1245;

controllerRouting(app);

app.listen(PORT, () => {
  console.log(`Example app. Listening on port ${PORT}`);
});

export default app;
