/*
  Warnings:

  - You are about to drop the column `edu_course` on the `OutputClEduCourse` table. All the data in the column will be lost.
  - Added the required column `program_id` to the `OutputClEduCourse` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "OutputClEduCourse" DROP COLUMN "edu_course",
ADD COLUMN     "program_id" INTEGER NOT NULL;

-- AddForeignKey
ALTER TABLE "OutputClEduCourse" ADD CONSTRAINT "OutputClEduCourse_program_id_fkey" FOREIGN KEY ("program_id") REFERENCES "Program"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "OutputClSimularCourse" ADD CONSTRAINT "OutputClSimularCourse_program_id_fkey" FOREIGN KEY ("program_id") REFERENCES "Program"("id") ON DELETE CASCADE ON UPDATE CASCADE;
