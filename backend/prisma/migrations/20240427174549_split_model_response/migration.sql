/*
  Warnings:

  - You are about to drop the column `response` on the `ModelResponse` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "ModelResponse" DROP COLUMN "response";

-- AddForeignKey
ALTER TABLE "OutputClEduCourses" ADD CONSTRAINT "OutputClEduCourses_response_id_fkey" FOREIGN KEY ("response_id") REFERENCES "ModelResponse"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "OutputClSimularCourse" ADD CONSTRAINT "OutputClSimularCourse_response_id_fkey" FOREIGN KEY ("response_id") REFERENCES "ModelResponse"("id") ON DELETE CASCADE ON UPDATE CASCADE;
