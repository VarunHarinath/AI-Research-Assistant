import Rpc from "../classes/RpcClient.js";

const getData = async (req, res) => {
  const data = req.body;
  res.json({ message: "received" });
  console.log(data.message);

  const rpc = new Rpc(data.message);
  await rpc.init();
  rpc.sendAndRecieveRpc();
};

export { getData };
