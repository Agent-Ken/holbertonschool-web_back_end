const weakMap = new WeakMap();

const queryAPI = (endpoint) => {
  let amount = weakMap.get(endpoint) || 0;

  amount += 1;

  weakMap.set(endpoint, amount);

  if (amount >= 5) {
    throw new Error('Endpoint load is high');
  }

  return amount;
};

export { weakMap, queryAPI };
