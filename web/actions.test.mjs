import assert from "node:assert/strict";
import test from "node:test";

import { bindSubmit, nextCounter } from "./actions.mjs";

test("submit button invokes its action", () => {
  let registeredHandler;
  const button = {
    addEventListener(event, handler) {
      assert.equal(event, "click");
      registeredHandler = handler;
    },
  };
  let submitted = false;
  bindSubmit(button, () => {
    submitted = true;
  });
  registeredHandler();
  assert.equal(submitted, true);
});

test("counter state advances consistently", () => {
  assert.equal(nextCounter(2), 3);
});
