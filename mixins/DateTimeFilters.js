import moment from "moment";

export const timeFormatter = {
  filters: {
    timeAgo(value) {
      return moment.utc(value).fromNow();
    },
  },
};