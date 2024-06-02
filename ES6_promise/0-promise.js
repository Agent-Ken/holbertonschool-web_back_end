// function that resolves or rejects 
function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const success = Math.random() > 0.5;
      if (success) {
        resolve({ data: 'This is a simulated successful response' });
      } else {
        reject(new Error('This is a simulated error'));
      }
    }, 1000);
  });
}

export default getResponseFromAPI;
