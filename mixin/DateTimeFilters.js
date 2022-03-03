import moment from "moment";

export var timeFormatter = {
  filters: {
    timeAgo(value) {
      return moment.utc(value).fromNow();
    },
  },
};

