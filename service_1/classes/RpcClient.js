import ampqlib from "amqplib";
import dotenv from "dotenv";
import { v4 as uuidv4 } from "uuid";

dotenv.config();

class Rpc {
  #url = process.env.URL;
  #EXCHANGE = process.env.EXCHANGE;

  constructor(job) {
    this.job = job;
    this.connection = null;
    this.channel = null;
  }

  async init() {
    this.connection = await ampqlib.connect(this.#url);
    this.channel = await this.connection.createChannel();
    await this.channel.assertExchange(this.#EXCHANGE, "direct", {
      durable: true,
    });
  }

  async sendAndRecieveRpc() {
    try {
      const generateCorrelationId = uuidv4();
      // Creating an Empty Queue
      const { queue: replyQueue } = await this.channel.assertQueue("", {
        exclusive: true,
      });
      // Receving The job
      this.channel.consume(replyQueue, (msg) => {
        if (msg.properties.correlationId === generateCorrelationId) {
          const result = JSON.parse(msg.content.toString());
          this.connection.close();
        }
      });

      // Sending the job
      this.channel.publish(
        this.#EXCHANGE,
        "summarize",
        Buffer.from(JSON.stringify(this.job), {
          replyTo: replyQueue,
          correlationId: generateCorrelationId,
        })
      );
      console.log("The job has been sent", this.job);
    } catch (error) {
      console.log(error);
    }
  }
}

export default Rpc;
