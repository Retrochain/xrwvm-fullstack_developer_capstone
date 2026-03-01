/*jshint esversion: 8 */

const express = require("express");
const mongoose = require("mongoose");
const fs = require("fs");
const cors = require("cors");
const bodyParser = require("body-parser");

const app = express();
const port = 3030;

app.use(cors());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(express.json());

const reviewsData = JSON.parse(
  fs.readFileSync("reviews.json", "utf8")
);
const dealershipsData = JSON.parse(
  fs.readFileSync("dealerships.json", "utf8")
);

mongoose.connect("mongodb://mongo_db:27017/", {
  dbName: "dealershipsDB",
});

const Reviews = require("./review");
const Dealerships = require("./dealership");

/* Seed Database */
(async function seedDatabase() {
  try {
    await Reviews.deleteMany({});
    await Reviews.insertMany(reviewsData.reviews);

    await Dealerships.deleteMany({});
    await Dealerships.insertMany(dealershipsData.dealerships);
  } catch (error) {
    console.error("Database seeding error:", error);
  }
})();

/* Home */
app.get("/", function (req, res) {
  res.send("Welcome to the Mongoose API");
});

/* Fetch all reviews */
app.get("/fetchReviews", async function (req, res) {
  try {
    const documents = await Reviews.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: "Error fetching documents" });
  }
});

/* Fetch reviews by dealer */
app.get("/fetchReviews/dealer/:id", async function (req, res) {
  try {
    const documents = await Reviews.find({
      dealership: req.params.id,
    });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: "Error fetching documents" });
  }
});

/* Fetch all dealerships */
app.get("/fetchDealers", async function (req, res) {
  try {
    const documents = await Dealerships.find();
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: "Error fetching documents" });
  }
});

/* Fetch dealerships by state */
app.get("/fetchDealers/:state", async function (req, res) {
  try {
    const documents = await Dealerships.find({
      state: req.params.state,
    });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: "Error fetching documents" });
  }
});

/* Fetch dealership by id */
app.get("/fetchDealer/:id", async function (req, res) {
  try {
    const documents = await Dealerships.find({
      id: req.params.id,
    });
    res.json(documents);
  } catch (error) {
    res.status(500).json({ error: "Error fetching documents" });
  }
});

/* Insert review */
app.post("/insert_review", async function (req, res) {
  try {
    const data = req.body;

    const documents = await Reviews.find()
      .sort({ id: -1 })
      .limit(1);

    const newId = documents.length > 0 ? documents[0].id + 1 : 1;

    const review = new Reviews({
      id: newId,
      name: data.name,
      dealership: data.dealership,
      review: data.review,
      purchase: data.purchase,
      purchase_date: data.purchase_date,
      car_make: data.car_make,
      car_model: data.car_model,
      car_year: data.car_year,
    });

    const savedReview = await review.save();
    res.json(savedReview);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Error inserting review" });
  }
});

/* Start server */
app.listen(port, function () {
  console.log(
    "Server is running on http://localhost:" + port
  );
});