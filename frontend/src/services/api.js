import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const generateQuiz = async (url) => {
  const response = await axios.post(`${API_URL}/generate_quiz`, { url });
  return response.data;
};

export const fetchHistory = async () => {
  const response = await axios.get(`${API_URL}/history`);
  return response.data;
};
