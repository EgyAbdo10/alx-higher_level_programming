#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

const userTasksCompleted = {};

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const records = JSON.parse(response.body);
  for (const rec of records) {
    if (rec.completed) {
      if (!(`${rec.userId}` in userTasksCompleted)) {
        userTasksCompleted[`${rec.userId}`] = 0;
      }
      userTasksCompleted[`${rec.userId}`] += 1;
    }
  }
  console.log(userTasksCompleted);
}
);
