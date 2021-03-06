const sharp = require('sharp');

module.exports = class respects extends ImageCode {
  static benchmark(constants) {
    return {
      avatar: constants.PICTURE1,
    };
  }

  async process(message) {
    const avatar = await sharp(await this.toBuffer(message.avatar))
      .resize(110, 110, { fit: 'cover' })
      .toBuffer();
    const metadata = await sharp(this.resource('respects.png')).metadata();
    const perspective = await this.perspectify(avatar, {
      topLeft: { x: 366, y: 91 },
      topRight: { x: 432, y: 91 },
      bottomLeft: { x: 378, y: 196 },
      bottomRight: { x: 439, y: 191 },
      canvas: {
        width: metadata.width,
        height: metadata.height,
        color: '#ddd',
      },
    });
    const canvas = sharp(this.resource('respects.png'))
      .composite([
        { input: perspective, left: 0, top: 0, blend: 'dest-over' },
      ]);

    return this.send(message, canvas);
  }
};

sharp({
                        create: {
                            width: 300,
                            height: 200,
                            channels: 4,
                            background: {
                                r: 255,
                                g: 0,
                                b: 0,
                                alpha: 0.5
                            }
                        }
                    })
                    .png()
                    .toFile('bungo.jpg')
                    .catch(function (error) {
                            console.error(error);
                        })
sharp(response.url)
                    .png()
                    .toFile('test.jpg')
                    .catch(function (error) {
                        console.error(error);
                    })