/*
  Warnings:

  - You are about to drop the `OutputClEduCourses` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "OutputClEduCourses" DROP CONSTRAINT "OutputClEduCourses_response_id_fkey";

-- DropTable
DROP TABLE "OutputClEduCourses";

-- CreateTable
CREATE TABLE "OutputClEduCourse" (
    "id" SERIAL NOT NULL,
    "response_id" INTEGER NOT NULL,
    "edu_course" INTEGER NOT NULL,

    CONSTRAINT "OutputClEduCourse_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "OutputClEduCourse" ADD CONSTRAINT "OutputClEduCourse_response_id_fkey" FOREIGN KEY ("response_id") REFERENCES "ModelResponse"("id") ON DELETE CASCADE ON UPDATE CASCADE;
