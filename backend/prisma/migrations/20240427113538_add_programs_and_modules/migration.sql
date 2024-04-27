-- CreateTable
CREATE TABLE "Program" (
    "id" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "speciality" TEXT NOT NULL,
    "url" TEXT NOT NULL,
    "tag" TEXT NOT NULL,
    "days_amount" INTEGER NOT NULL,
    "price" INTEGER NOT NULL,

    CONSTRAINT "Program_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Module" (
    "id" INTEGER NOT NULL,
    "program_id" INTEGER NOT NULL,
    "title" TEXT NOT NULL,
    "ordinal" INTEGER NOT NULL,

    CONSTRAINT "Module_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Quarter" (
    "id" INTEGER NOT NULL,
    "program_id" INTEGER NOT NULL,
    "title" TEXT NOT NULL,
    "ordinal" INTEGER NOT NULL,

    CONSTRAINT "Quarter_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Module" ADD CONSTRAINT "Module_program_id_fkey" FOREIGN KEY ("program_id") REFERENCES "Program"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Quarter" ADD CONSTRAINT "Quarter_program_id_fkey" FOREIGN KEY ("program_id") REFERENCES "Program"("id") ON DELETE CASCADE ON UPDATE CASCADE;
