-- AlterTable
ALTER TABLE "Module" ALTER COLUMN "title" DROP NOT NULL;

-- AlterTable
ALTER TABLE "Program" ALTER COLUMN "speciality" DROP NOT NULL,
ALTER COLUMN "url" DROP NOT NULL,
ALTER COLUMN "tag" DROP NOT NULL,
ALTER COLUMN "days_amount" DROP NOT NULL,
ALTER COLUMN "price" DROP NOT NULL,
ALTER COLUMN "difficulty" DROP NOT NULL;
