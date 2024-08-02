#!/usr/bin/node

const url = 'https://jsonplaceholder.typicode.com/todos';
const request = require('request');

const userTasksCompleted = {};

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const records = JSON.parse(response.body);
  for (let userId = 1; userId < 11; userId++) {
    let tasksCompleted = 0;
    let rec;
    for (rec of records) {
      if (rec.userId === userId) {
        if (rec.completed) {
          tasksCompleted += 1;
        }
      }
    }
    if (tasksCompleted > 0) {
      userTasksCompleted[`${userId}`] = tasksCompleted;
    }
  }
  console.log(userTasksCompleted);
}
);
