const cleanSet = (set, startString) => {
  const strng = [];

  if (
    typeof set !== 'object'
    || typeof startString !== 'string'
    || startString.length === 0
  ) {
    return '';
  }

  for (const item of set) {
    if (item && item.startsWith(startString)) {
      strng.push(item.slice(startString.length));
    }
  }

  return strng.join('-');
};

export default cleanSet;
