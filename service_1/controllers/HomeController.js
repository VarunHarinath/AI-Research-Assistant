const HomeController = (req, res) => {
  try {
    res.json({ message: "The api is accessed" });
    res.status(200);
  } catch (error) {
    res.json(error);
    res.status(505);
  }
};
export { HomeController };
