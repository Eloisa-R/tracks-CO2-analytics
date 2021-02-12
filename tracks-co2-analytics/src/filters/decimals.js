import humanize from 'humanize';

const roundUp = (value) => {
  if (!value) {
    return 0.00;
  }
  return humanize.numberFormat(value, 2);
};

export default roundUp;
