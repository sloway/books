module.exports = (sequelize, DataTypes) => (
  sequelize.define('hashtag', {
    title: {
      type: DataTypes.STRING(15),
      allowNull: false,
      unqiue: true,
    },
  }, {
    timestamps: true,
    paranoid: true,
  })
);
